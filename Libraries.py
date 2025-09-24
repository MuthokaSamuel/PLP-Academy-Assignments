import os
import requests
from urllib.parse import urlparse
import uuid


def fetch_images():

    urls = input("Enter one or more image URLs separated by commas: ").strip().split(",")

    directory = "Fetched_Images"

    os.makedirs(directory, exist_ok=True)

    for url in urls:

        url = url.strip()

        if not url:
            continue

        try:
            response = requests.get(url, timeout=10)

            response.raise_for_status()


            parsed_url = urlparse(url)

            filename = os.path.basename(parsed_url.path)


            if not filename or "." not in filename:

                filename = f"image_{uuid.uuid4().hex}.jpg"


            filepath = os.path.join(directory, filename)


            with open(filepath, "wb") as file:

                file.write(response.content)

            print(f"✅ Image saved as: {filepath}")

        except requests.exceptions.MissingSchema:

            print(f"❌ Error: '{url}' is invalid. Please include http:// or https://")

        except requests.exceptions.ConnectionError:

            print(f"❌ Error: Could not connect to '{url}'")

        except requests.exceptions.Timeout:

            print(f"❌ Error: Request to '{url}' timed out")

        except requests.exceptions.HTTPError as http_err:

            print(f"❌ HTTP Error for '{url}': {http_err}")

        except Exception as err:

            print(f"❌ Unexpected error for '{url}': {err}")


if __name__ == "__main__":
    fetch_images()
