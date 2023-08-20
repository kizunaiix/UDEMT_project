import os

dirs = os.listdir("./all_results")


for i in dirs:
    check1 = os.path.exists(f"./all_results/{i}/{i}.ply")
    if check1 == False:
        print(f"{i}.ply  : lost")

    check2 = os.path.exists(f"./all_results/{i}/0_center.off")
    if check2 == False:
        print(f"{i}/0_center.off  : lost")

    check3 = os.path.exists(f"./all_results/{i}/0_input.off")
    if check3 == False:
        print(f"{i}/0_input.off  : lost")

    check4 = os.path.exists(f"./all_results/{i}/0_mesh_graph.obj")
    if check4 == False:
        print(f"{i}/0_mesh_graph.obj  : lost")
    
    check5 = os.path.exists(f"./all_results/{i}/0_skel_edge.obj")
    if check5 == False:
        print(f"{i}/0_skel_edge.obj  : lost")
    
    check6 = os.path.exists(f"./all_results/{i}/0_skel_face.obj")
    if check6 == False:
        print(f"{i}/0_skel_face.obj  : lost")

    check7 = os.path.exists(f"./all_results/{i}/0_sphere.obj")
    if check7 == False:
        print(f"{i}/0_sphere.obj  : lost")




print("good")