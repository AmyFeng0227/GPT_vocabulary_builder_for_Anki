# GPT Vocabulary Builder for Anki

This tool establishes a seamless integration between the custom GPT, named **"Vocabulary Builder for Anki,"** and your Anki deck. You can access the GPT using the following link: [Vocabulary Builder for Anki](https://chatgpt.com/g/g-6786d57ebe1c819195c1cf11142b2b6c-vocabulary-builder-with-anki). It offers translations and examples for English or Swedish words and automatically adds them to your specified Anki deck.

### Key Features

- **Learning**:
  - Translates words into Chinese, English, and Swedish effortlessly.
  - Provides example sentences for better context and understanding.
  - Offers insights into how commonly a word is used to enhance learning efficiency.
- **Integration with Anki**: Seamlessly connects with your Anki decks via AnkiConnect, adding notes directly to your specified deck upon request.

### **Important**

Your computer, Anki app, and local tunnel need to be on and running for the tool to work. 

---

## Step 1: Setting Up Anki (Skip if you already have Anki)

1. Download and install Anki:
   - [Anki Download Page](https://apps.ankiweb.net/)
   - Follow the installation instructions for your operating system.
2. Create a deck where you want to store the generated cards.

---

## Step 2: Installing AnkiConnect

1. Open Anki.
2. Go to `Tools > Add-ons > Get Add-ons`.
3. Enter the following code to install AnkiConnect:
   - **2055492159**
4. Click `OK` and wait for the installation to complete.
5. Restart Anki to activate AnkiConnect.

---

## Step 3: Setting Up LocalTunnel and Your AnkiConnect URL

Before sharing your details, you need to set up a LocalTunnel to make your AnkiConnect accessible to this tool. This step allows the tool to communicate with your Anki deck securely over the internet by creating a unique, static web address for your local AnkiConnect server.

### Install Node.js:

1. Go to the official [Node.js download page](https://nodejs.org/en).
2. Download the **LTS (Long-Term Support)** version for your operating system.
3. Follow the installation prompts specific to your operating system.
4. Ensure the installer **adds Node.js and npm to your system's PATH**.

### Install LocalTunnel:

1. Open the command prompt or terminal:

   - **On Windows**:
     - Press `Win + R` to open the Run dialog.
     - Type `cmd` and press `Enter`.
   - **On macOS**:
     - Press `Cmd + Space` to open Spotlight Search.
     - Type `Terminal` and press `Enter`.

2. Copy and paste the following command to install LocalTunnel:

   ```
   npm install -g localtunnel
   ```

3. Start a LocalTunnel with a static unique URL by running the following command. Replace `yourcustomsubdomain` with a unique name (e.g., "amysankiconnector", "myankivocabularybuilder1234"). The name must be unique globally on the internet, as duplicate names will prevent the URL from being created:

   ```
   lt --port 8765 --subdomain yourcustomsubdomain
   ```

4. Save this command somewhere, as you will need to run it every time you restart the command prompt.

5. A URL will be created and shown in the command prompt (e.g., `https://yourcustomsubdomain.loca.lt`), which will be used for sharing in the next step.

---

## Step 4: Sharing Your Details

Email the following information to [fengshangchanhui@gmail.com](mailto\:fengshangchanhui@gmail.com):

1. **Username**: Your desired username for this tool. (You will always be asked for your username when starting a new chat.)
2. **AnkiConnect URL**: The URL you generated in Step 3.
3. **Deck Name**: The name of the deck where you want the vocabulary cards to be added.

### Example Email:

```
Subject: GPT Vocabulary Builder for Anki

Hello,

I would like to use the GPT Vocabulary Builder for Anki. Here are my details:
- Username: [Your Username]
- AnkiConnect URL: [Your URL created in Step 3]
- Deck Name: [Your Deck Name]

Thank you!
```

---

## You're All Set!

Once your setup is complete, I will configure the tool to work with your Anki.

### Each time before using the tool:

1. Ensure your computer is on.
2. Open Anki.
3. Open the command prompt and run the following command. Replace "yourcustomsubdomain" with your real subdomain name that you saved earlier.
   ```
   lt --port 8765 --subdomain yourcustomsubdomain
   ```

## Happy learning!

