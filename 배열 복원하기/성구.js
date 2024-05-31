// 16967 배열 복원하기

const fs = require('fs');

const setting = () => {
    // const input = fs.readFileSync('input.txt').toString().split("\n");
    const input = fs.readFileSync('/dev/stdin').toString().split("\n");
    const [H, W, X, Y] = input[0].split(" ").map(Number);
    const B = [];
    for (let i=0;i<H+X;i++){
        B.push(input[i+1].split(" ").map(Number));
    }
    return [H, W, X, Y, B];
}


const main = (H, W, X, Y, B)=> {
    const A = Array(H);
    for (let i=0;i<H;i++) A[i] = new Array(W).fill(0);

    for (let i=0;i<H;i++){
        for (let j=0;j<W;j++){
            A[i][j] = B[i][j];

            if (0 <= i-X && i-X < H && 0 <= j-Y && j-Y < W){
                A[i][j] -= A[i-X][j-Y];
            }
        
        }
        console.log(...A[i]);
    }   
}


const [H, W, X, Y, B] = setting();
main(H, W, X, Y, B);