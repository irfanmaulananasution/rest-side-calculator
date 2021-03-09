from braces.views import CsrfExemptMixin
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#https://www.django-rest-framework.org/api-guide/status-codes/
#https://stackoverflow.com/a/34316546/4921103
#https://www.django-rest-framework.org/api-guide/requests/#query_params
class Calculator(CsrfExemptMixin, APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        print(request.data)
        try:
            var1 = float(request.data['var1'])
            var2 = float(request.data['var2'])
            operation = request.data['operation']
            if operation == 'addition':
                result = var1 + var2
            elif operation == 'substraction':
                result = var1 - var2
            elif operation == 'multiplication':
                result = var1 * var2
            elif operation == 'division':
                result = var1 / var2
            else:
                raise ValueError
            
            json_result_response = {
                'input' : {
                           'var1' : request.data['var1'],
                           'var2' : request.data['var2'],
                           'operation' : request.data['operation']
                          },
                'output' : result
            }
            return Response(json_result_response)
        except ValueError:
            return Response({}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
