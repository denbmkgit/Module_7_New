class WorldFinder:
    file_names = []


    def __init__(self, *names_files):
        for name_file in names_files:
            self.file_names.append(name_file)

    def get_all_worlds(self,):
        all_words = {}
        for name in self.file_names:
            with name



        print(all_words)
        #     for str_ in file:
        #         pass



wf = WorldFinder('file1.txt', 'file2.txt', 'file3.txt')
print(wf.file_names)

# for i in wf.file_names:
#     print(i)

wf.get_all_worlds()