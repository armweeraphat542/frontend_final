import { METHODS } from 'http'
import { error} from '@sveltejs/kit';
import { create } from "domain";

//load train โดย query id จาก params
export async function load({ params, url }) {
    const trainId = url.searchParams.get('id');
    const res = await fetch(`http://localhost:3000/trains/${trainId}`);
    const booktrain = await res.json();

    if (!booktrain) throw error(404);

    return {
        booktrain
    };
}

// POST และ Update ตามข้อมูลรถไฟและฟอร์ม
export const actions = {
    create: async ({ request }) => {
        try {
            const data = await request.formData();

            const trainId = data.get('trainId');

            const trainRes = await fetch(`http://localhost:3000/trains/${trainId}`);
            if (!trainRes.ok) {
                throw new Error('Failed to fetch train data!');
            }
            const train = await trainRes.json();
            const seatNumbers = data.getAll('seatNumbers');

           

            const booking = {
                name: data.get('name'),
                contactNumber: data.get('contactNumber'),
                trainid: train.id,
                trainNumber: train.trainNumber,
                departure: train.departure,
                arrival: train.arrival,
                departureTime: train.departureTime,
                arrivalTime: train.arrivalTime,
                totalprice: train.price * seatNumbers.length,
                passenger: seatNumbers.length,
                seatNumbers
            };

            const res = await fetch('http://localhost:3000/bookings', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(booking)
            });

            if (!res.ok) {
                throw new Error('Booking failed!');
            }

            const updateRes = await fetch(`http://localhost:3000/trains/${trainId}`, {
                
                method: 'PATCH',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ availableSeats: train.availableSeats - seatNumbers.length })
            });
            
           

            if (!updateRes.ok) {
                alert('Failed to update available seats!');
            } else {
                alert('Booking successful!');
                
            }
            
        } catch (error) {
            return {
                status: 500,
                body: { error: 'Failed' }
            };
        }
    }
};








  


