## Cartoony Image API
- Overview

The Cartoony Image API is a fun service that transforms uploaded images into cartoon-like versions using image processing techniques. It's built with FastAPI and OpenCV, providing a simple yet entertaining way to cartoonize your images.

# Features
* Cartoonize any uploaded image
* Supports various image formats
* Real-time transformation with fast response times
* Easy integration with any application or platform
# Requirements
* Python 3.x
* FastAPI
* OpenCV
# Installation
Clone the repository:

```
git clone <repository_url>
cd <repository_directory>
```
Install dependencies:
```
pip install -r requirements.txt
```
## Usage
Start the FastAPI server:

```
uvicorn main:app --reload
```
Access the Cartoony Image API endpoints:

Upload an image to cartoonize: http://localhost:8000/cartoony_image [POST]
# API Documentation
You can explore and test the API using the Swagger UI documentation:
http://localhost:8000/docs

How it Works
The API applies image processing techniques to simplify the colors and edges in the uploaded image, resulting in a cartoon-like appearance.

Examples
Original Image:

![1](./sajjad.jpg)

Cartoony Image:

![1](./cartoon.png)
