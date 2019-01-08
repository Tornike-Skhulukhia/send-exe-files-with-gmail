'''
    About us:
    
        Youtube Channel:  bit.ly/shencshegidzlia
        Facebook Page  :  fb.me/shencshegidzlia
        Email:            info.shencshegidzlia@gmail.com

        შენც შეგიძლია!
        28.05.2018
        
'''


def help_():
        result = """
		ფაილი შეიცავს ფუნქციებს, რომლებიც გვეხმარებიან მითითებულ საქაღალდეში მარტივად შევცვალოთ ყველა ფაილის გაფართოება,
		მათთვის ბოლოში ჩვენთვის სასურველი ტექსტის დამატებით/მოშორებით. სასურველია სრული მისამართების(Full Paths) გამოყენება.

		მისი გამოყენების ერთი მაგალითია Gmail.com-ზე მრავალრიცხოვან ფაილშემცველი პროგრამების გადაგზავნა იმეილით, რომელთა სტანდარტულად გაგზავნაც
		შეუძლებელია, უსაფრთხოების პარამეტრების გამო. გაგზავნამდე საჭიროა ფაილებს გაფართოებაში encrypt ფუნქციით დავუმატოთ სასურველი ტექსტი და
		მიმღებმა ანალოგიური მნიშვნელობებით გამოიყენოს decrypt ფუნქცია.

		ვთქვათ, ფაილები მდებარეობს საქაღალდეში, რომლის მისამართია C:\\Users\\user\\Desktop\\Files,

			Encrypt('C:\\Users\\user\\Desktop\\Files', '.pdf')
			ამ საქაღალდის ყველა ფაილს გადააქცევს არსებულ სახელს +  '.pdf' .
			მაგალითად 'ფაილი.txt' ==> 'ფაილი.txt.pdf' 

			ფუნქციები მოქმედებისას გვიბეჭდავს ფაილების მისამართებს, რომლებსაც შეეხო ოპერაცია.
			თუ ფაილს უკვე აქვს ასეთი დანამატი, მისი მეორედ დამატება და დაბეჭდვა აღარ მოხდება, ანალოგიური პრინციპი ვრცელდება მოშორების შემთხვევაშიც.
		
		გაფრთხილება:
			ფუნქციების მიზანი საგანმანათლებლობა, ნუ გამოიყენებთ მათ ადამიანთათვის ზიანის მისაყენებლად.

	"""
        return result


def get_file_locations(files_folder):
    ''' Function gets all file paths from folder '''
    # import
    import os
    ''' save all files relative location here '''
    all_paths = []
    ''' get files locations '''
    for dirPath, dirNames, fileNames in os.walk(files_folder):
        
        new_paths = [os.path.join(dirPath, fileName) for fileName in fileNames]

        all_paths += new_paths # += instead of append
    # return result
    return all_paths


def encrypt(files_folder, extension_to_add):
    ''' Function adds second argument string to each files extension text in given folder(if file does not have this text added already) '''
    # import
    import os
    # get paths using previous function
    paths = get_file_locations(files_folder)
    
    for old_file_path in paths:
        # get folders relative location and file name separately
        folder_location, file_name =  os.path.dirname(old_file_path), os.path.basename(old_file_path)
        # rename file (add new text in extension part)
        # check that file does not contain this text already at the end
        if not file_name.endswith(extension_to_add):
            new_file_name = file_name + extension_to_add  
            # define new relative path
            new_file_path = os.path.join(folder_location, new_file_name)
            # rename
            os.rename(old_file_path, new_file_path)
            # print
            print(folder_location.ljust(50), file_name.ljust(40), "| + |" )
            
     
def decrypt(files_folder, extension_to_remove):
    ''' Function removes second argument string from each files extension text in given folder(if it is possible to remove) '''
    # import
    import os
    # get full paths using previous function
    paths = get_file_locations(files_folder)

    # ! bad practice --> code is repeated
    for old_file_path in paths:
        # get folders relative location and file name separately
        folder_location, file_name =  os.path.dirname(old_file_path), os.path.basename(old_file_path)
        # rename file (add new text in extension part)
        # check that file does not contain this text already at the end
        if file_name.endswith(extension_to_remove):
            new_file_name = file_name[ : (len(file_name) - len(extension_to_remove))]
            # define new relative path
            new_file_path = os.path.join(folder_location, new_file_name)
            # rename
            os.rename(old_file_path, new_file_path)
            # print
            print(folder_location.ljust(50), file_name.ljust(40), "| + |" )


