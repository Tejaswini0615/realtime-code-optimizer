import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

def start_lsp_server():
    """Start the Python LSP Server (pylsp)"""
    try:
        logging.info("Starting Python LSP Server...")
        subprocess.run(["pylsp"], check=True)
    except Exception as e:
        logging.error(f"Failed to start LSP server: {e}")

if __name__ == "__main__":
    start_lsp_server()
    
    
