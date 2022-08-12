import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
  else:

    # seperating the list into matrix
    arr1=[]
    arr1.append(list[0:3])
    arr1.append(list[3:6])
    arr1.append(list[6:])
    calculations={}

    # seperating the vertical axis
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
    var_axis11=np.var(axis11)
    var_axis12=np.var(axis12)
    var_axis13=np.var(axis13)
    
    var_axis21=np.var(list[0:3])
    var_axis22=np.var(list[3:6])
    var_axis23=np.var(list[6:])

    var_flat=np.var(list)
    
    arr_var_axis1=[var_axis11,var_axis12,var_axis13]
    arr_var_axis2=[var_axis21,var_axis22,var_axis23]
    arr_final_var=[arr_var_axis1,arr_var_axis2,var_flat]
    calculations["variance"]=arr_final_var


    # standard devation
    std_axis11=np.std(axis11)
    std_axis12=np.std(axis12)
    std_axis13=np.std(axis13)
    
    std_axis21=np.std(list[0:3])
    std_axis22=np.std(list[3:6])
    std_axis23=np.std(list[6:])

    std_flat=np.std(list)
    
    arr_std_axis1=[std_axis11,std_axis12,std_axis13]
    arr_std_axis2=[std_axis21,std_axis22,std_axis23]
    arr_final_std=[arr_std_axis1,arr_std_axis2,std_flat]
    calculations["standard deviation"]=arr_final_std

    # max
    max_axis11=max(axis11)
    max_axis12=max(axis12)
    max_axis13=max(axis13)
    
    max_axis21=max(list[0:3])
    max_axis22=max(list[3:6])
    max_axis23=max(list[6:])

    max_flat=max(list)
    
    arr_max_axis1=[max_axis11,max_axis12,max_axis13]
    arr_max_axis2=[max_axis21,max_axis22,max_axis23]
    arr_final_max=[arr_max_axis1,arr_max_axis2,max_flat]
    calculations["max"]=arr_final_max

    # min
    min_axis11=min(axis11)
    min_axis12=min(axis12)
    min_axis13=min(axis13)
    
    min_axis21=min(list[0:3])
    min_axis22=min(list[3:6])
    min_axis23=min(list[6:])

    min_flat=min(list)
    
    arr_min_axis1=[min_axis11,min_axis12,min_axis13]
    arr_min_axis2=[min_axis21,min_axis22,min_axis23]
    arr_final_min=[arr_min_axis1,arr_min_axis2,min_flat]
    calculations["min"]=arr_final_min

    # sum
    sum_axis11=sum(axis11)
    sum_axis12=sum(axis12)
    sum_axis13=sum(axis13)
    
    sum_axis21=sum(list[0:3])
    sum_axis22=sum(list[3:6])
    sum_axis23=sum(list[6:])

    sum_flat=sum(list)
    
    arr_sum_axis1=[sum_axis11,sum_axis12,sum_axis13]
    arr_sum_axis2=[sum_axis21,sum_axis22,sum_axis23]
    arr_final_sum=[arr_sum_axis1,arr_sum_axis2,sum_flat]
    calculations["sum"]=arr_final_sum

    
  return calculations