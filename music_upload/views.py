from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from music_upload.models import Music
from music_upload.serializers import MusicUploadSerializer
from music_upload.permissions import IsOwnerOrReadOnly
# Create your views here.


class MusicUploadView(APIView):
    '''
        Handles music upload
    '''
    serializer_class = MusicUploadSerializer
    permission_classes = (IsAuthenticated,)


    def post(self, request):

        data = request.data
        user = request.user

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():

            if data.get("upload_type") == "PRO":
                allowed_users = data.get("allowed_users")
                if allowed_users:
                    for allowed_user in allowed_users:
                        if not User.objects.all().filter(id=allowed_user).exists():
                            return Response({"message": "You can only allow users who have registered to the app."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"message": "You have to choose users who can access this music."}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save(user=user)
        
            return Response({"data":serializer.data, "message":"New Music file uploaded"}, status=status.HTTP_201_CREATED)

        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    


class MusicListView(APIView):

    serializer = MusicUploadSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user = request.user
        music = Music.objects.all().order_by('-uploaded_on')
        public_music = music.filter(upload_type="PUB")
        private_music = music.filter(upload_type="PRI", user=user)
        protected_music = music.filter(upload_type="PRO", allowed_users=user)
        queryset = (public_music | private_music | protected_music).distinct()        
        serializer = self.serializer(queryset, many=True)
        return Response({"data":serializer.data, "message":"List of music"}, status=status.HTTP_200_OK)



class MusicDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = MusicUploadSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, )
    queryset = Music.objects.all()


    def get(self, request, *args, **kwargs):

        music = self.get_object()
        serializer = self.serializer_class(music)
        if music.upload_type == "PRO":
            if request.user not in music.allowed_users.all():
                return Response({"message": "You are not allowed to view this music."}, status=status.HTTP_403_FORBIDDEN)
        
        if music.upload_type == "PRI":
            if request.user != music.user:
                return Response({"message": "You are not allowed to view this music."}, status=status.HTTP_403_FORBIDDEN)
        
        return Response({"data":serializer.data, "message":"Music details"}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        print(request.data)
        return super().update(request, *args, **kwargs)