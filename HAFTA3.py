
# coding: utf-8

# In[43]:

#MATRİS ÇARPMAYI KODLAYACAĞIZ
# matrix_1 mxn
# matrix_2 nxp
# matrix_3=matrix_1 * matrix_2 , mxp


# In[44]:

def get_value_from_row_col(r_1,c_1):        #Karmaşıklık O(n)  (Boyutları aynı olmak zorunda)
    t=0
    for i in range(len(r_1)):
        t=t+r_1[i]*c_1[i]
    return t
a=[1,2,3,4]
b=[5,6,7,8]
get_value_from_row_col(a,b)


# In[45]:

b=[[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]] # 4x4
a=[[1,2,3,4],[5,6,7,8]]                     # 2x4


# In[46]:

def get_row_from_matrix(a,i):
    return a[i]
def get_col_from_matrix(a,j):
    col=[]
    for row in a:
        col.append(row[j])
#     for row in a:
#         for indis in range(len(row)):
#             if(indis==j):
#                 col.append(row[indis])
    return col
a=[[1,2,3,4],[5,6,7,8]]                     # 2x4
get_col_from_matrix(a,1) 


# In[47]:

def matrix_multiply(m_1,m_2):  #Karmaşıklık O(mnp), kare matris olursa O(n^3)
    m=len(m_1)
    n=len(m_2[0])
    r=[]
    for i in range(m):
        r.append([])
        for j in range(n):
            a=get_row_from_matrix(m_1,i)
            b=get_col_from_matrix(m_2,j)
            c=get_value_from_row_col(a,b)
            r[i].append(c)
    return r
a=[[1,2,3,4],[5,6,7,8]]     # 2x4
b=[[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]     # 4x4
matrix_multiply(a,b)


# In[48]:

def matrix_multiply(m_1,m_2):
    m=len(m_1)
    n=len(m_2[0])
    r=[]
    for i in range(m):
        r.append([])
        for j in range(n):
            a=get_row_from_matrix(m_1,i)
            b=get_col_from_matrix(m_2,j)
            c=get_value_from_row_col(a,b)
            r[i].append(c)
    return r


# In[ ]:



