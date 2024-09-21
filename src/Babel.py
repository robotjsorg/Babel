class Babel:
    def __init__(self):
        self.languageServers = []
    
    def addLanguageServer(self, langServer):
        if serverPaid(langServer):
            self.languageServers.append(langServer)
        else:
            print("")
    
    def server(self):
        # some API call
    
    def provideServer(self):
        for server in self.languageServers:
            service(server)