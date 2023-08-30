#include <stdio.h> 
#include <stdlib.h>
int source,V,E,time,visited[20],G[20][20]; 
void DFS(int i,int n,int a[],int k)
{
	
	int j; visited[i]=1;
	if(i==n)
	{
		for(j=0;j<k;j++)
		{
			printf("%d -> ",a[j]+1);
		}
		exit(0);
	}
	for(j=0;j<V;j++)
	{
		if(G[i][j]==1&&visited[j]==0)
		{
			a[k]=j;
			DFS(j,n,a,k+1);
		}
	}
}
int main()
{
	int i,j,v1,v2,n,k=1; 
	int a[10];
	for(i=0;i<10;i++)
	{
		a[i]=0;
	}
	printf("\t\t\tGraphs\n"); 
	printf("Enter the no of edges:"); 
	scanf("%d",&E);
	printf("Enter the no of vertices:"); 
	scanf("%d",&V);
	for(i=0;i<V;i++)
	{
		for(j=0;j<V;j++)
		{
			G[i][j]=0;
		}
	}
	for(i=0;i<E;i++)
	{
		printf("Enter the edges (format: V1 V2) : ");
		scanf("%d%d",&v1,&v2);
		G[v1-1][v2-1]=1;
		G[v2-1][v1-1]=1;
	}
	for(i=0;i<V;i++)
	{
		for(j=0;j<V;j++)
		{
			printf(" %d ",G[i][j]);
		}
		printf("\n");
	}
	printf("Enter the source: "); 
	scanf("%d",&source);
	printf("Enter Goal: ");
	scanf("%d",&n);
	a[0]=source-1;
	DFS(source-1,n-1,a,k); 
	return 0;
}