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
    
    def server(self):
        pass
        # some API call
    
    def provideServer(self):
        for server in self.languageServers:
            service(server)