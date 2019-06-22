from rest_framework_jwt.utils import jwt_decode_handler

def getUserId(request):
  authorization = request.META['HTTP_AUTHORIZATION']
  token = authorization.replace('Bearer ', '')
  token = jwt_decode_handler(token)
  userId = token['user_id']
  return userId