// 3109 빵집
const fs = require("fs");

const settings = () => {
    const input = fs.readFileSync("input.txt").toString().trim().split("\n");
    // const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
    const [R, C] = input[0].split(" ").map(Number);
    const ground = [];
    input.slice(1).forEach((e) => ground.push(e));
    return [R, C, ground];
}


const main = (R, C, ground) => {
    const makePipeLine = (row) => {
        const stack = [[row, 0]];
        
        while (stack.length > 0) {
            const [i, j] = stack.pop();
            visited[i][j] = 1
            if ( j === C-1) return true;

            for (let di = 1; di > -2; di --){
                const [ni,nj] = [di+i, j+1];
                if (0<=ni && ni <R && nj < C && ground[ni][nj] !== "x" && visited[ni][nj] !== 1){
                    stack.push([ni,nj]);
                }
            }

        }   
        return false;
    }
    let cnt = 0;
    const visited = [];
    for (let r=0; r<R;r++){
        visited.push(Array(C).fill(0));
    }


    for (let i=0; i<R; i++){
        if (ground[i][0] !== "x"){
            cnt += makePipeLine(i);
        }
    }
    console.log(cnt);
}

const [R, C, ground] = settings();

main(R, C, ground);
