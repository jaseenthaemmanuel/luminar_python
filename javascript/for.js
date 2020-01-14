var r=Number( prompt("input the number"));
var i;
var flag=0;
for(i=2;i<r;i++)
{
    for(j=2;j<i;j++)
    {
        if(i%j==0)
        {
        flag=1;
        break;
        }
        else
        {
            flag=0;
        }
    }
    if(flag!=1)
    {
    console.log(i)
    }
}
