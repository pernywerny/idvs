import requests, os, json




class APILib:
    def __init__(self):
        self.user_data = None
        self.response = None
        self.api_link = None
        self.host = 'http://127.0.0.1:8000'
        self.api_url = 'idvs/api/'




    def verifyDocument(self, agency, document_type, document_id):
        if self.host:
            self.user_data = {
                                "agency_id": agency,
                                "doctype_id": document_type,
                                "doc_id": document_id
                            }
            
            # self.api_link = f"{self.host}/{self.api_url}/document/"
            self.response = requests.post("http://127.0.0.1:8000/idvs/api/document", json = self.user_data)

            data = self.response.json()
            status_code = self.response.status_code

            if status_code == 200:
                return data
            
            else:
                data = {
                            'status_code': status_code,
                            'error': self.response
                        }
                return data