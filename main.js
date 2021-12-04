function SoNguyenTo(n){
    if(n < 2){
        return false;
    } else{
        for(let i = 2; i <= Math.sqrt(n); i++){
            if(n%i===0){
                return false;
            }
        }
        return true;
    }
}

function songuyentocuahaiso(trai,phai){
    let arr = [];
    for(let i = trai; i < phai; i++){
        if(SoNguyenTo(i) === true){
            arr.push(i);
        }
    }
    return arr;
}

let find = document.querySelector('#bai2');
let result = document.querySelector('.result');
find.addEventListener('click', () => {
    let trai = document.querySelector("#left-number").value;
    let phai = document.querySelector("#right-number").value;
    let primeNumberArr = songuyentocuahaiso(trai,phai);
    result.innerHTML += `<p>Số nguyên tố trong khoảng (${trai};${phai}) là ${primeNumberArr}</p>`;
})
