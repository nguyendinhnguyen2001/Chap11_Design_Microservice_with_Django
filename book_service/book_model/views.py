from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

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
def book(request):

    if request.method == 'GET':  # user requesting data
        snippets = Book.objects.all()
        serializer = BookSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # user posting data
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def book_detail(request,pk):

    if request.method == 'GET': 
        snippet = Book.objects.get(pk=pk)
        serializer = BookSerializer(snippet)
        return Response(serializer.data)