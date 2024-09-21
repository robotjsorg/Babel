import logging

class Babel:
    def __init__(self):
        self.languageServers = []
    
    def serverPaid(self, langServer) -> bool:
        return langServer.paid
    
    def addLanguageServer(self, langServer):
        if self.serverPaid(langServer):
            self.languageServers.append(langServer)
            logging.info(f"Added language server: {langServer}")
        else:
            logging.warning(f"Failed to add language server: {langServer} (not paid)")
    
    def translateService(self, message: str, sourceLang: str, targetLang: str):
        # some API call
        return f"Translated '{message}' from {source_lang} to {target_lang}"
    
    def provideService(self, message: str, targetLang: str):
        for server in self.languageServers:
            while server.events:
                event = server.events.popleft()
                logging.info(f"Processing Event: {event} for {server}")
                translatedMessage = self.translateService(event, server.language, targetLang)