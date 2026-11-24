pip install deepface
from deepface import DeepFace

image1 = "person1.jpg"
image2 = "person2.jpg"

result = DeepFace.verify(
    img1_path=image1,
    img2_path=image2,
    model_name="Facenet512"
)

print("Face Recognition Result")

if result["verified"]:
    print("Both images contain a matching face.")
else:
    print("The faces do not match.")

print("Distance:", round(result["distance"], 4))
print("Model:", result["model"])
