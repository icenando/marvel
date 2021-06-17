INSTALLATION

1. Open a developer account at[https://developer.marvel.com]() .
2. Once registered, take note of your public and private API keys.
3. Download this code.
4. Open Mac Terminal by pressing CMD + spacebar and typing Terminal. Enter the marvel-main folder:

   ```
   cd marvel-main
   ```
5. Create and activate a virtual environment (below is one named .venv - the dot makes it invisible):

   ```
   python3 -m venv .venv
   . .venv/bin/activate
   ```
6. Install the necessary packages listed in requirements.txt using pip :

   ```
   pip install -r requirements.txt
   ```
7. Run the code:

   ```
   gunicorn app:app
   ```
8. Open your browser and enter the following in the address line:

   ```
   localhost:8000
   ```
9. You should now see the description of the story at the top of the page, followed by the characters that feature in it (alongside their profile images), and Marvel's attribution text at the bottom of the page.
