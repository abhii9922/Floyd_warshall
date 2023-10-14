from Data_Collection.data_collect import data_collect
from Algo.algo import FWAlgorithm

distance_matrix=data_collect("Fullerton,California,USA",33.8781, -117.87957,33.87827, -117.87968,500)
"""
The above function returns the following like:
Sample Distance Matrix={(11203244427, 11203244428): 14.239, 
(11203244428, 3077720345): 8.466,
(3077720345, 11203244429): 8.662,
(3077720345, 3583764515): 141.787,
(3583764515, 122562951): 13.611,
(122562951, 9393624778): 7.306,
(9393624778, 11203244426): 140.612,
(11203244426, 9393624783): 12.51,
(9393624783, 9393624786): 80.983,
(9393624786, 3533840250): 7.591,
(3533840250, 3077720341): 53.885,
(3077720341, 122900932): 16.677,
(122900932, 11203244432): 10.447,
(11203244432, 11203244434): 19.303,
(11203244434, 9393624802): 15.263,
(9393624802, 9393624804): 12.616,
(9393624804, 9393624805): 22.192,
(9393624805, 9393624806): 38.901,
(9393624806, 9393624808): 52.561, 
(9393624808, 9393624809): 23.008,
(9393624809, 11203244429): 7.738,and many more}
"""

fw_obj=FWAlgorithm()

distance_dict,path_dict=fw_obj.initalize(distance_matrix)
"""
Sample:
Distancr_dict={(101, 101): 0, (101, 102): 5, (101, 104): 6, (101, 105): 100000, (101, 103): 100000, (102, 101): 100000, (102, 102): 0, (102, 104): 100000, (102, 105): 7, (102, 103): 1, (104, 101): 100000, (104, 102): 100000, (104, 104): 0, (104, 105): 3, (104, 103): 2, (105, 101): 2, (105, 102): 100000, (105, 104): 5, (105, 105): 0, (105, 103): 100000, (103, 101): 3, (103, 102): 100000, (103, 104): 4, (103, 105): 100000, (103, 103): 0}
Path_dict={(101, 101): [101], (101, 102): [101, 102], (101, 104): [101, 104], (101, 105): [], (101, 103): [], (102, 101): [], (102, 102): [102], (102, 104): [], (102, 105): [102, 105], (102, 103): [102, 103], (104, 101): [], (104, 102): [], (104, 104): [104], (104, 105): [104, 105], (104, 103): [104, 103], (105, 101): [105, 101], (105, 102): [], (105, 104): [105, 104], (105, 105): [105], (105, 103): [], (103, 101): [103, 101], (103, 102): [], (103, 104): [103, 104], (103, 105): [], (103, 103): [103]}
"""

distance_dict,path_dict=fw_obj.compute_distance_matrix()
"""
Sample:
Disrance_dict={(101, 101): 0, (101, 102): 5, (101, 104): 6, (101, 105): 9, (101, 103): 6, (102, 101): 4, (102, 102): 0, (102, 104): 5, (102, 105): 7, (102, 103): 1, (104, 101): 5, (104, 102): 10, (104, 104): 0, (104, 105): 3, (104, 103): 2, (105, 101): 2, (105, 102): 7, (105, 104): 5, (105, 105): 0, (105, 103): 7, (103, 101): 3, (103, 102): 8, (103, 104): 4, (103, 105): 7, (103, 103): 0}
Path_dict={(101, 101): [101], (101, 102): [101, 102], (101, 104): [101, 104], (101, 105): [101, 104, 105], (101, 103): [101, 102, 103], (102, 101): [102, 103, 101], (102, 102): [102], (102, 104): [102, 103, 104], (102, 105): [102, 105], (102, 103): [102, 103], (104, 101): [104, 105, 101], (104, 102): [104, 105, 101, 102], (104, 104): [104], (104, 105): [104, 105], (104, 103): [104, 103], (105, 101): [105, 101], (105, 102): [105, 101, 102], (105, 104): [105, 104], (105, 105): [105], (105, 103): [105, 104, 103], (103, 101): [103, 101], (103, 102): [103, 101, 102], (103, 104): [103, 104], (103, 105): [103, 104, 105], (103, 103): [103]}
"""

#distance_dict,path_dict=fw_obj.remove_edges([(102,103),(103,104),(102,105)])

#distance_dict,path_dict=fw_obj.add_edges({(102,103):0.5,(105,103):3})
