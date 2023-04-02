from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Clothe_detail
from .serializers import ClotheSerializer

# {
# "book_id":'1',
# "title":'OnePiece', 
# "auther":'Oda', 
# "description":'phieu luu hanh dong',
# "availability":'san dung', 
# "publisher":'KimDong',
#  "publish_Date":'20/031998', 
# "price":'22000'
# }
@api_view(['GET', 'POST'])
def clothe(request):

    if request.method == 'GET':  # user requesting data
        snippets = Clothe_detail.objects.all()
        serializer = ClotheSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # user posting data
        serializer = ClotheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def clothe_detail(request,pk):

    if request.method == 'GET': 
        snippet = Clothe_detail.objects.get(pk=pk)
        serializer = ClotheSerializer(snippet)
        return Response(serializer.data)