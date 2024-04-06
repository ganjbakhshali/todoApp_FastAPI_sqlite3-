import io
import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse

app = FastAPI()

def cartoonize_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.bilateralFilter(gray, 9, 75, 75)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 75, 75)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon

@app.post("/cartoonize_image")
async def cartoonize_image_endpoint(input_file: UploadFile = File(...)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Unsupported file type")

    contents = await input_file.read()
    np_array = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    cartoon_image = cartoonize_image(image)

    _, image_encoded = cv2.imencode(".jpg", cartoon_image)
    image_bytes = image_encoded.tobytes()
    
    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/jpeg")
