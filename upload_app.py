import tkinter as tk
from tkinter import filedialog
from google.cloud import storage
import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_CLOUD_BUCKET_NAME = os.environ['GOOGLE_CLOUD_BUCKET_NAME']
credentials_dict= {
            "type": os.environ['GCP_type'],
            "project_id": os.environ['GCP_project_id'],
            "private_key_id": os.environ['GCP_private_key_id'],
            "private_key": os.environ['GCP_private_key'],
            "client_email": os.environ['GCP_client_email'],
            "client_id": os.environ['GCP_client_id'],
            "auth_uri": os.environ['GCP_auth_uri'],
            "token_uri": os.environ['GCP_token_uri'],
            "auth_provider_x509_cert_url": os.environ['GCP_auth_provider_x509_cert_url'],
            "client_x509_cert_url": os.environ['GCP_client_x509_cert_url'],
            "universe_domain": os.environ['GCP_universe_domain']
            }
# Define your credentials (replace with your own)
client = storage.Client.from_service_account_info(credentials_dict)
def upload_image_to_gcs():
    """ Uploads images to google cloud which are uploaded by frontend """
    try:
        filename = filedialog.askopenfilename()  # Opens file dialog to select the image file
        if filename:
            file_basename = os.path.basename(filename)
            # Create a blob object
            blob = client.bucket(GOOGLE_CLOUD_BUCKET_NAME).blob(file_basename)
            # Upload the image
            blob.upload_from_filename(filename)
            print(f'{filename} uploaded to Google Cloud Storage to {GOOGLE_CLOUD_BUCKET_NAME}')
            # Display a success message
            tk.messagebox.showinfo("Success", f"{file_basename} uploaded to {GOOGLE_CLOUD_BUCKET_NAME}")
    except Exception as e:
        print(e)
        tk.messagebox.showerror("ERROR", f"Upload failure check logs: {e}")

def initialize_ui(closing_message = ""):
    # Create the tkinter window
    window = tk.Tk()
    window.title("Image Upload to Google Cloud Storage")

    # Create a button to upload the image
    upload_button = tk.Button(window, text="Upload Image to GCS", command=upload_image_to_gcs)
    upload_button.pack(pady=20)

    # Run the tkinter main loop
    window.mainloop()
    return closing_message

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialize_ui()

