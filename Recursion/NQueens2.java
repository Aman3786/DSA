'''
N Queen2:- Count the number of different arrangements of Queen on Chessboard
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
    
    int solve(int n,int row, char[][] mat){
        if(row == n){
            return 1;
        }
        
        int count = 0;
        for(int col = 0; col < n; col++){
            if(check(n,row,col,mat)){
                mat[row][col] = 'Q';
                count += solve(n,row+1,mat);
                mat[row][col] = '.';
            }
        }
        
        return count;
    }
    public int totalNQueens(int n) {
        Solution sol = new Solution();
        char[][] mat = new char[n][n];
        for(int i = 0; i < n; i++){
            Arrays.fill(mat[i],'.');
        }
        int res = sol.solve(n,0,mat);
        return res;
    }
}
