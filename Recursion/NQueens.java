'''
N Queen:- Get all the distinct arrangement of a Queen on Chessboard
'''

class Solution {
    boolean check(int n, int row, int col, char[][] mat){
        int r = row;
        int c = col;
         
        while(r > 0){
            if(mat[--r][c] =='Q') return false;
        }
        
        r = row;
        c = col;
        while(r > 0 && c > 0){
            if(mat[--r][--c] == 'Q') return false;
        }
        
        r = row;
        c = col;
        while(r > 0 && c < n-1){
            if(mat[--r][++c] == 'Q') return false;
        }
        
        return true;
    }
    
    void solve(int n,int row, char[][] mat, List<List<String>> ans){
        if(row == n){
            List<String> temp = new ArrayList<String>();
            
            for(int i = 0;i<n;i++){
                String s = new String(mat[i]);
                temp.add(s);
                
            }
            ans.add(temp);
            return;
        }
        
        for(int col = 0; col < n; col++){
            if(check(n,row,col,mat)){
                mat[row][col] = 'Q';
                solve(n,row+1,mat,ans);
                mat[row][col] = '.';
            }
        }
    }
    
    public List<List<String>> solveNQueens(int n) {
        Solution sol = new Solution();
        List<List<String>> ans = new ArrayList<>();
        char[][] mat = new char[n][n];
        for(int i = 0; i < n; i++){
            Arrays.fill(mat[i],'.');
        }
        sol.solve(n,0,mat,ans);
        return ans;
        
        
    }
}
        
        