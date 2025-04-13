import streamlit as st
import hashlib
import json
import time
import os
from datetime import datetime
from cryptography.fernet import Fernet
from typing import Optional, Dict, Any

# Constants
MAX_ATTEMPTS: int = 3
LOCKOUT_TIME: int = 300  # 5 minutes
DATA_FILE: str = "encrypted_data.json"
KEY_FILE: str = "secret.key"
MASTER_PASSWORD_HASH: str = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"  # sha256 of "admin"


# ---streamlit config---
st.set_page_config(
    page_title="Secure Data Encryption System",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Helper Functions ---

def generate_or_load_key() -> bytes:
    """Load or generate Fernet encryption key."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key

def load_data() -> Dict[str, Any]:
    """Load encrypted data from JSON file."""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data: Dict[str, Any]) -> None:
    """Save encrypted data to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def hash_passkey(passkey: str, salt: Optional[str] = None) -> str:
    """Hash a passkey with optional salt."""
    salt = salt or os.urandom(16).hex()
    hash_bytes = hashlib.pbkdf2_hmac('sha256', passkey.encode(), salt.encode(), 100000)
    return f"{salt}${hash_bytes.hex()}"

def verify_passkey(passkey: str, stored_hash: str) -> bool:
    """Verify a passkey against a stored hash."""
    try:
        salt, stored = stored_hash.split("$")
        new_hash = hashlib.pbkdf2_hmac('sha256', passkey.encode(), salt.encode(), 100000).hex()
        return stored == new_hash
    except Exception:
        return False

def encrypt_data(text: str, cipher: Fernet) -> str:
    """Encrypt data using Fernet."""
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(token: str, cipher: Fernet) -> Optional[str]:
    """Decrypt data using Fernet."""
    try:
        return cipher.decrypt(token.encode()).decode()
    except Exception:
        return None

def check_lockout() -> bool:
    """Check if the user is currently locked out."""
    if st.session_state.get("locked_out", False):
        elapsed = time.time() - st.session_state.get("lockout_time", 0)
        if elapsed < LOCKOUT_TIME:
            st.error(f"🔒 Locked out. Try again in {int(LOCKOUT_TIME - elapsed)} seconds.")
            return True
        else:
            st.session_state.locked_out = False
            st.session_state.failed_attempts = 0
    return False

# --- Setup ---

cipher = Fernet(generate_or_load_key())
stored_data = load_data()

# --- Streamlit Session State Initialization ---
st.session_state.setdefault("failed_attempts", 0)
st.session_state.setdefault("locked_out", False)
st.session_state.setdefault("lockout_time", 0)
st.session_state.setdefault("authenticated", False)

# --- Sidebar ---
st.sidebar.title("Navigation")
if st.session_state.locked_out and check_lockout():
    menu = ["Home", "Login"]
else:
    menu = ["Home", "Store Data", "Retrieve Data", "Login"] if st.session_state.authenticated else ["Home", "Login"]

choice = st.sidebar.selectbox("Choose", options=menu)

# --- Main Area ---

st.title("🔐 Secure Data Encryption System")

# --- Home ---
if choice == "Home":
    st.subheader("🏠 Welcome")
    st.write("Securely **store** and **retrieve** encrypted data with your unique passkey.")
    if st.session_state.authenticated:
        st.success("✅ You are logged in. Thre are some bugs that I will be fixing soon. as I got time I will fix them.")
        st.info("This is a simple data encryption system. use admin as username and admin as password to login. this is just a sample cradentials never use them in production.")
        st.write("Use the sidebar to navigate.")
        st.write("You can store and retrieve encrypted data.")
        st.write("Your data is encrypted with a unique passkey.")
    else:
        st.warning("Please log in to access full functionality. Thre are some bugs that I will be fixing soon. as I got time I will fix them.")
        st.info("This is a simple data encryption system. use admin as username and admin as password to login. this is just a sample cradentials never use them in production.")
        st.write("Use the sidebar to navigate.")
        st.write("You can store and retrieve encrypted data.")
        st.write("Your data is encrypted with a unique passkey.")

# --- Login ---
elif choice == "Login":
    st.subheader("🔑 Login")

    if st.session_state.authenticated:
        st.success("Already logged in.")
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.failed_attempts = 0
            st.session_state.locked_out = False
            st.rerun()
    else:
        if check_lockout():
            st.stop()

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "admin" and hashlib.sha256(password.encode()).hexdigest() == MASTER_PASSWORD_HASH:
                st.session_state.authenticated = True
                st.session_state.failed_attempts = 0
                st.session_state.locked_out = False
                st.success("✅ Login successful!")
                time.sleep(1)
                st.rerun()
            else:
                st.session_state.failed_attempts += 1
                remaining = MAX_ATTEMPTS - st.session_state.failed_attempts

                if remaining > 0:
                    st.error(f"❌ Incorrect credentials! {remaining} attempts left.")
                else:
                    st.session_state.locked_out = True
                    st.session_state.lockout_time = time.time()
                    st.error("🚫 Too many failed attempts. Locked out for 5 minutes.")
                    st.rerun()

# --- Store Data ---
elif choice == "Store Data":
    if not st.session_state.authenticated:
        st.warning("Please login first.")
        st.stop()

    st.subheader("📦 Store Encrypted Data")

    name = st.text_input("Data Name")
    content = st.text_area("Data to Encrypt")
    passkey = st.text_input("Passkey", type="password")
    confirm = st.text_input("Confirm Passkey", type="password")

    if st.button("Encrypt & Store"):
        if not name or not content or not passkey:
            st.error("All fields are required.")
        elif passkey != confirm:
            st.error("Passkeys do not match.")
        elif name in stored_data:
            st.error("Data name already exists. Choose another.")
        else:
            hashed = hash_passkey(passkey)
            encrypted = encrypt_data(content, cipher)
            stored_data[name] = {
                "encrypted_text": encrypted,
                "passkey_hash": hashed,
                "timestamp": datetime.now().isoformat()
            }
            save_data(stored_data)
            st.success("✅ Data encrypted and saved.")
            st.json({
                "data_name": name,
                "status": "encrypted",
                "timestamp": stored_data[name]["timestamp"]
            })

# --- Retrieve Data ---
elif choice == "Retrieve Data":
    if not st.session_state.authenticated:
        st.warning("Please login first.")
        st.stop()

    if check_lockout():
        st.stop()

    st.subheader("📥 Retrieve Encrypted Data")

    if not stored_data:
        st.warning("No data to retrieve.")
    else:
        name = st.selectbox("Select Entry", list(stored_data.keys()))
        passkey = st.text_input("Passkey", type="password", key="decrypt_key")

        if st.button("Decrypt"):
            entry = stored_data.get(name)

            if not passkey:
                st.error("Enter your passkey.")
            elif verify_passkey(passkey, entry["passkey_hash"]):
                decrypted = decrypt_data(entry["encrypted_text"], cipher)
                if decrypted:
                    st.success("✅ Decryption successful!")
                    st.text_area("Decrypted Data", value=decrypted, height=200)
                    st.caption(f"Stored on: {datetime.fromisoformat(entry['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
                    st.session_state.failed_attempts = 0
                else:
                    st.error("❌ Decryption error.")
            else:
                st.session_state.failed_attempts += 1
                left = MAX_ATTEMPTS - st.session_state.failed_attempts
                if left > 0:
                    st.error(f"❌ Wrong passkey! {left} attempts remaining.")
                else:
                    st.session_state.locked_out = True
                    st.session_state.lockout_time = time.time()
                    st.error("🔒 Locked out after too many failed attempts.")
                    st.rerun()

# --- Sidebar System Info ---
st.sidebar.markdown("---")
st.sidebar.subheader("System Info")
if st.session_state.authenticated:
    st.sidebar.success("Logged In ✅")
else:
    st.sidebar.warning("Not Authenticated")

if st.session_state.locked_out:
    remaining = int(max(0, LOCKOUT_TIME - (time.time() - st.session_state.lockout_time)))
    st.sidebar.error(f"⏳ Lockout: {remaining}s left")
else:
    st.sidebar.info(f"Attempts used: {st.session_state.failed_attempts}/{MAX_ATTEMPTS}")

st.sidebar.markdown(f"🔐 Encrypted Entries: {len(stored_data)}")
