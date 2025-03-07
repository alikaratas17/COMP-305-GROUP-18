#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void sort_numbers(int*,int);
int insert_numbers(int*,int*,int,int);
void calculate_sums(long*,int*,int,int);
void calculate_orders(int *,long*,int);
void compare_orders(int*,int*,int);
int main(int argc, char * argv[]){
  char* filename = argv[1];//"./Test Cases/baby_comp_4.txt";
  char * outputFilename = "./outputs/outputC.txt";
  FILE * fpOut;
  FILE * fp;
  fp = fopen(filename, "r");
  int n,m;
  fscanf(fp,"%d",&n);
  fscanf(fp,"%d",&m);
  int num;

  int i = 0;
  int numbers[n][m];
  while (i<n){
    int j = 0;
    while(j<m){
      fscanf(fp,"%d",&num);
      numbers[i][j] = num;
      j++;
    }
    sort_numbers(numbers[i],m);
    
    i++;
  }
  fclose(fp);
  
  int l_values [n*m];
  int size = insert_numbers(l_values,numbers,n,m);
  long sums[n];
  
  calculate_sums(sums,numbers,n,m);
  /*for(int i = 0;i< n;i++)
    printf("%d ",sums[i]);
  printf("\n");*/
  int min_orders [n];
  int orders [n];
  calculate_orders(orders,sums,n);
  /*for(int i = 0;i< n;i++)
    printf("%d ",orders[i]);
  printf("\n");*/
  
  int k[n];
  for (int i=0;i<n;i++){
    k[i]=0;
    min_orders[i] = orders[i];
  }
  
  int old_l = l_values[0];
  int l;
  for(int i = 0; i< size;i++){
    l = l_values[i];
    for(int j = 0; j < n;j++){
      sums[j] += (k[j]* (l - old_l));
      int dv = 0;
      if (k[j]<m){
        while(numbers[j][k[j]] >= l){
          dv += (numbers[j][k[j]] - l);
          k[j]++;
          if (k[j]==m)
            break;
        }
      }
      sums[j]-=dv;
    }
    calculate_orders(orders,sums,n);
    compare_orders(min_orders,orders,n);
   /* for(int j_1 = 0;j_1< n;j_1++)
    printf("%d ",sums[j_1]);
      printf("\n");*/
      /* for(int j_1 = 0;j_1< n;j_1++)
    printf("%d ",orders[j_1]);
      printf("\n");*/
    old_l = l;
  }
  fpOut = fopen(outputFilename, "w");
  for(int i = 0;i<n;i++)
    fprintf(fpOut,"%d\n",min_orders[i]);
  fclose(fpOut);


  return 0;
}
//sort_numbers sorts numbers[i] in descending order using insertion sort
void sort_numbers(int * array,int length){
  for (int i = 0; i<length;i++){
    int j = i;
    while(j > 0 && array[j-1] < array[j]){
      int temp = array[j];
      array[j] = array[j-1];
      array[j-1] = temp;
      j --;
    }
  }
}


// numbers[i][j]-> *((numbers+m*i)+j)
int insert_numbers(int * l_values,int * numbers,int n,int m){
  int current[n];
  for (int i = 0;i < n;i++){
    current[i]=0;
  }
  int max_index = 0;
  int max = 0;
  int index = 0;

  for(int i = 0; i< n;i++){

      if (*((numbers+m*i)+0)> max){
        max = *((numbers+m*i)+0);
        max_index = i;
      }else if(*((numbers+m*i)+0)== max){
        
        current[i]++;
        while(*((numbers+m*i)+current[i])== max){
          if(current[i]==m)
            break;
          current[i]++;
          }
      }
    }

  l_values[0] = max;
  while((*((numbers+m*max_index)+current[max_index]))== max){
    if (current[max_index]==m)
      break;
    current[max_index]++;
  }
  while(1){
    index ++;
    max = 0;
    max_index = -1;
    for(int i = 0; i< n;i++){
      if(current[i]==m)
        continue;
      if (*((numbers+m*i)+current[i])>max){
        max = *((numbers+m*i)+current[i]);
        max_index = i;
      }else if(*((numbers+m*i)+current[i])== max){
        current[i]++;
        while(1){
          if (current[i]==m || *((numbers+m*i)+current[i])!= max)
            break;
          current[i]++;
          }
      }
    }
    if (max == 0)
      return index;
    l_values[index] = max;
    while(*((numbers+m*max_index)+current[max_index])== max){
    if (current[max_index]==m)
      break;
    current[max_index]++;
  }
  }

  return index;
}

void calculate_sums(long * sums,int * numbers,int n,int m){
  int num;
  for (int i= 0;i<n;i++){
    sums[i]=0;
    for (int j= 0;j<m;j++){
      num = *((numbers+m*i)+j);
      sums[i] += num;
    }
  }
  return;
}

//Update 
void calculate_orders(int *orders,long* sums,int n){
  int indexes [n];
  long s_copy[n];
  for (int i = 0;i<n;i++){
    indexes[i] = i;
    s_copy[i]= sums[i];
  }
  for (int i = 0; i<n;i++){
    int j = i;
    while(j > 0 && ( s_copy[j-1]<  s_copy[j])){
      long temp = s_copy[j];
      s_copy[j] = s_copy[j-1];
      s_copy[j-1] = temp;
      int temp2 = indexes[j-1];
      indexes[j-1]=indexes[j];
      indexes[j] = temp2;
      j --;
    }
  }
  int o = n;
  orders[indexes[0]]=o;
  o--;
  for(int i =1;i<n;i++){
    if(s_copy[i] <  s_copy[i-1]){
      orders[indexes[i]]=o;
    }else{
      orders[indexes[i]]=orders[indexes[i-1]];
    }
    o--;
  }
  return;
}
//Update current min orders using orders
void compare_orders(int * min_orders,int *orders,int n){
  for (int i= 0;i<n;i++){
    if(orders[i]<min_orders[i])
      min_orders[i]=orders[i];
  }
  return;
}