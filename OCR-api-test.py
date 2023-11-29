from google.cloud import documentai_v1 as documentai

project_id = 'my-documentai-codelab'
location = 'us'
processor_id = '71380215b0b268e6'
file_path = '/Users/User/PycharmProjects/Images/sumatriptan label.jpeg'
mime_type = 'image/jpeg'  # Correct MIME type for a JPEG image

# Read the image file
with open(file_path, 'rb') as image:
    image_content = image.read()

# Configure the processor client
opts = {
    "api_endpoint": "us-documentai.googleapis.com"  # Correct API endpoint format
}
client = documentai.DocumentProcessorServiceClient(client_options=opts)

# Construct the request
name = client.processor_path(project_id, location, processor_id)
raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)
request = documentai.ProcessRequest(name=name, raw_document=raw_document)  # Named arguments

# Process the document
result = client.process_document(request=request)  # Named argument for request
document = result.document

# Check if the document has been processed successfully
if document.text:
    print("Document Text:")
    print(document.text)

    # Other details can be printed similarly depending on your requirements
else:
    print("No text found in the document.")
