import logging
import google.generativeai as genai

class Babel:
    def __init__(self):
        self.languageServers = []
        genai.configure(api_key="AIzaSyA7DBv7BrmTVZWzt6Gv7LjVhDd_ehHtIp4")

        generation_config = {
            "temperature": 0.2,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are Babel, the friendly Discord translation service."
        )
    
    def serverPaid(self, langServer) -> bool:
        return langServer.paid
    
    def addLanguageServer(self, langServer):
        if self.serverPaid(langServer):
            self.languageServers.append(langServer)
            logging.info(f"Added language server: {langServer}")
        else:
            logging.warning(f"Failed to add language server: {langServer} (not paid)")
    
    def translateService(self, message: str, sourceLang: str, targetLang: str):
        
        prompt = f"Translate from {sourceLang} to {targetLang}: {message}"
        chat_session = self.model.start_chat(history=[{"role": "user", "parts": [prompt]}])
        response = chat_session.send_message("Translate")
        return response.text
    
    def provideService(self, message: str, targetLang: str):
        for server in self.languageServers:
            while server.events:
                event = server.events.popleft()
                logging.info(f"Processing Event: {event} for {server}")
                translatedMessage = self.translateService(event, server.language, targetLang)
                logging.info(f"Translated Message: {translatedMessage}")