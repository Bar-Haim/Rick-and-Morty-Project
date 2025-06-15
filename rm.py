import requests
import csv
import time

time.sleep(15)  # המתנה של 10 שניות כדי לאפשר DNS להתחבר

url = 'https://rickandmortyapi.com/api/character' 
mylist = []  

def rnm():
    current_url = url  # מתחילים מהעמוד הראשון

    # כל עוד יש עוד עמוד להמשיך אליו
    while current_url:
        try:
            response = requests.get(current_url)
            response.raise_for_status()  # מוודא שהתקבלה תגובה תקינה
            result = response.json()
        except Exception as e:
            print(f"שגיאה בגישה ל-API: {e}")
            break  # יוצאים מהלולאה אם יש שגיאה

        for character in result["results"]:
            if (
                character["species"] == "Human"
                and character["status"] == "Alive"
                and character["origin"]["name"] == "Earth (Replacement Dimension)"
            ):
                mylist.append({
                    'name': character["name"],
                    'location': character["origin"]["name"],
                    'image': character["image"],
                })

        # נעדכן את current_url לקישור לעמוד הבא
        current_url = result["info"]["next"]

    return mylist

characters = rnm()

# ✨ שמירת התוצאה ל־CSV כולל origin ו־image
with open("characters.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "location", "image"])
    writer.writeheader()
    writer.writerows(characters)

print("הקובץ characters.csv נוצר בהצלחה!")
