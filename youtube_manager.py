import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("*"*100)
    for index,video in enumerate(videos,1):
        print(f"{index}. Video Name : {video["name"]}, Time : {video["time"]}")
    print("*"*100)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
    
def update_video(videos):
    list_all_videos(videos)
    selectIndex = int(input("Select the number of the Video that you want to Update : "))
    
    if 1 <=selectIndex <= len(videos):
        video = input("Enter new Video Name : ")
        time = input("Enter new Video Time : ")
        
        videos[selectIndex-1] = {'name':video, 'time':time }
        save_data_helper(videos)
        print("Updated Successfully")

def delete_video(videos):
    list_all_videos(videos)
    deleteIndex = int(input("Select the number of the Video that you want to Delete : "))
    
    if 1 <= deleteIndex <= len(videos):
        del videos[deleteIndex-1]
        save_data_helper(videos)
        print(f"video has been deleted")
    else:
        print("Invalid Index Selected")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("\n 1. List all Videos")
        print("\n 2. Add a Video")
        print("\n 3. Update Details")
        print("\n 4. Delete a Video")
        print("\n 5. Exit the App")
        choice = input("\n Enter your Choice : ")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice")          
                
                

if __name__ == "__main__":
    main()