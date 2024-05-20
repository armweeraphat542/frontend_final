import { METHODS } from 'http'

export async function load() {
    const res = await fetch('http://localhost:3000/trains'); 
    const trains = await res.json(); //เก็บข้อมูล trains ทั้งหมดไว้ในตัวแปร

    // เอาแค่ สถานีต้นทางและปลายทางแบบซุ้ำกันเอาอันเดียว
    // @ts-ignore
    const stations = Array.from(new Set(trains.flatMap(train => [train.departure, train.arrival])));

    //ส่งคือข้อมูลรถไฟและสถานี
    return {
        trains,
        stations
    };
}
