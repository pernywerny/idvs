from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from .models import *
from .serializers import DocumentSerializer




class DocumentView(APIView):
    def get(self, request):
        return Response({'message': 'success',}, status = status.HTTP_200_OK)
        # docs = get_object_or_404(Document, issuing_agency = agency, document_id = doc_id)
        # doc_ser = DocumentSerializer(docs, many = False)
        # return Response(doc_ser.data, status = 200)


    def post(self, request):
        doc_type = request.data.get('doctype_id')
        agency = request.data.get('agency_id')
        doc_id = request.data.get('doc_id')


        if not all([doc_type, agency, doc_id]):
            print('missing fields')
            missing_fields = []

            if not doc_type: missing_fields.append(doc_type)
            if not agency: missing_fields.append(agency)
            if not doc_id: missing_fields.append(doc_id)

            response = {
                            'is_verified': False,
                            "message": "Missing required information",
                            "missing fields": missing_fields
                        }

            return Response(response, status = status.HTTP_400_BAD_REQUEST)
        
        else:
            try: doc = Document.objects.get(issuing_agency_id = agency, document_type_id = doc_type, document_id = doc_id)
            except: doc = None

           
            if doc:
                owner_name = f"{doc.owner.fname} {doc.owner.oth_names} {doc.owner.lname}"
                data_packet = {
                                    "is_verified": True,
                                    "message": "Document has been verified to be genuine",
                                    "document_data": {
                                                        "document_id": doc.document_id,
                                                        "owner_name": owner_name,
                                                    }
                                }
                return Response(data_packet, status = status.HTTP_200_OK)
                

            else:
                data_packet = {
                                    "is_verified": False,
                                    "message": "Document could not be verified"
                                }
                
                return Response(data_packet, status = status.HTTP_404_NOT_FOUND)
            
            data_packet = {
                                    "is_verified": False,
                                    "message": "Document could not be verified"
                                }
            
            return Response(data_packet, status = status.HTTP_404_NOT_FOUND)
