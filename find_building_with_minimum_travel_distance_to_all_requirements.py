
# This is my solution to the question asked by Clément Mihailescu in this youtube video [ Link: https://www.youtube.com/watch?v=rw4s4M3hFfs&t=516s ].
# It is really far from good but it works. Let's optimize and make it better!
# Credit to "@alex nice" in the comments section of the Youtube video for his suggestion. Thank you mate!

blocks = [
    {
      'gym': False,
      'school': True,
      'store': False
    }, 
    {
      'gym': True,
      'school': False,
      'store': False
    }, 
    {
      'gym': True,
      'school': True,
      'store': False
    }, 
    {
      'gym': False,
      'school': True,
      'store': False
    }, 
    {
      'gym': False,
      'school': True,
      'store': True
    }
]
Reqs = ['gym', 'school', 'store']


max_distances = []
distances = {}


def check_val(row, key):
    if blocks[row][key] == True:
        return 0
    else:
        ans = []
        checkList = list([k for (k, v) in enumerate(blocks) if v[key] is True])

        for index in checkList:  
            dist = abs(index - i)
            ans.append(dist)

        return min(ans)


for i, j in enumerate(blocks):
    for k in j:
        res = check_val(i, k)
        if i not in distances:
            distances[i] = [res]
        else:
            distances[i].append(res)


for key, values in distances.items():
    max_distances.append(max(values))


index_min = min(max_distances, key=max_distances.__getitem__)
best_building_block = blocks[index_min]
print(f'The best building to live in is the building with index of {index_min} whose values are {best_building_block}')



