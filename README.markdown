ABOUT

This one page app retrieves the information about one of my favourite X-Men stories featuring Bobby Drake (aka: Iceman). It was published in January 1997 in Uncanny X-Men 340. The page shows the description of the story and the characters that appear in this issue.

It is a simple programme that uses the Marvel's developers API, written in python and flask in the backend.

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
6. Install the necessary packages listed in requirements.txt using pip

   ```
   pip install -r requirements.txt
   ```
7. Now you need to export the public and private API keys that you received when you joined Marvel as environment variables, as follows:

   ```
   export API_PUBLIC='your_public_API_key_goes_here'
   export API_PRIVATE='your_private_API_key_goes_here'
   ```
8. Run the code:

   ```
   gunicorn app:app
   ```
9. Open your browser and enter the following in the address line:

   ```
   localhost:8000
   ```
10. You should now see the description of the story at the top of the page, followed by the characters that feature in it (alongside their profile images), and Marvel's attribution text at the bottom of the page.

   ![marvel_screenshot](https://github.com/icenando/marvel/assets/20210618_111059_Screenshot_2021-06-18 at 11.09.41.png?raw=true)
