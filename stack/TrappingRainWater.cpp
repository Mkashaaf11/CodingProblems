class Solution {
public:

    int trap(vector<int>& height) {
int n=height.size();
vector<int> leftMax(n);
vector<int> rightMax(n);
leftMax[0]=height[0];
rightMax[n-1]=height[n-1];
int sum=0;
//calculating leftMax
for(int i=1;i<n;i++)
{
    leftMax[i]=max(leftMax[i-1],height[i]);
}
//calculating rightMax
for(int i=n-2;i>=0;i--)
{
    rightMax[i]=max(rightMax[i+1],height[i]);
}

for(int i=0;i<n;i++)
{
    int water=min(leftMax[i],rightMax[i])-height[i];
    sum=sum+water;

}

return sum;
        
    }
};