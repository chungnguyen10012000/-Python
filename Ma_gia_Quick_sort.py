procedure quicksort(left, right: integer);
var j, k: integer;
begin
    if right > left then
    begin
    j:=left - 1; k:=right;
    repeat
        repeat j:=j+1 until a[j] >= a[right];
        repeat k:=k-1 until a[k]<= a[right];
        if j< k then swap(a[j],a[k])
    until j>k;
    swap(a[right],a[j]);
    quicksort(left,j-1);
    quicksort(j+1,right)
    end;
end;