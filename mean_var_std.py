import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
  else:
    arr1=[]
    arr1.append(list[0:3])
    arr1.append(list[3:6])
    arr1.append(list[6:])
    calculations={}
    axis11=[list[0],list[3],list[6]]
    axis12=[list[1],list[4],list[7]]
    axis13=[list[2],list[5],list[8]]
    # mean
    mean_axis11=np.mean(axis11)
    mean_axis12=np.mean(axis12)
    mean_axis13=np.mean(axis13)
  
    mean_axis21=np.mean(list[0:3])
    mean_axis22=np.mean(list[3:6])
    mean_axis23=np.mean(list[6:])   
        
    mean_flat=np.mean(list)
    arr_mean_axis1=[mean_axis11,mean_axis12,mean_axis13]
    arr_mean_axis2=[mean_axis21,mean_axis22,mean_axis23]
    arr_final_mean=[arr_mean_axis1,arr_mean_axis2,mean_flat]
    calculations["mean"]=arr_final_mean

    # variance
    
  return calculations