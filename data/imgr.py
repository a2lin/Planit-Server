from imgurpython import ImgurClient

client_id = '080b68c1dc5b420'
client_secret = '83f44f1ca138abef40c5d6c16b24b9b14320db6c'

client = ImgurClient(client_id, client_secret)

def searchImage(description):
   paths = client.gallery_search(description, sort='viral')

   for path in paths:
      path = path.link
      if path.endswith(".jpg") or path.endswith(".png"):
         return path

   #no suitable image found
   return ""


