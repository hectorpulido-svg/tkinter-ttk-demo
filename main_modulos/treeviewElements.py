import json
import sys
import os


class LOADJSONDOC:
    def __init__(self):
        self.parents = []
        self.childs = []

    def readDoc(self, file):
        self.file = file
        with open(self.file, 'r') as file:
            self.data = json.load(file)
            tree = self.data['tree']
        for elements in tree:
            for key in elements.keys():
                values = elements[key]
                if key == 'parent':
                    self.parents.append(values)
                elif key == 'childs':
                    self.childs.append(values)

        # print(self.parents)
        # print(self.childs)
    
    def loadParents(self):
        # print(len(json.dumps(self.parents)))
        return self.parents
    def loadChilds(self):
        return self.childs


def loadTester():
    parents = r.loadParents()
    childs = r.loadChilds()
    for pi, parent in enumerate(parents):
        print('PARENT PROPERTIES: parent: %s, index: %d, text: %s, iid: %s, tags: %s' %(
        parent['parent'], parent['index'], parent['text'], parent['iid'], parent['tags']))
        for child in childs[pi]:
            print('CHILD PROPERTIES parent: %s, index: %d. text: %s, iid: %s, tags: %s' %(
                child['parent'], child['index'], child['text'], child['iid'], child['tags']
            ))



                    

if __name__ == '__main__':
    cwd = os.path.sys.path[0]
    file = os.path.join(cwd, 'treeviewElements.json')
    r = LOADJSONDOC()
    r.readDoc(file)
    loadTester()
else:
    pass