import { METHODS } from 'http'
import { error} from '@sveltejs/kit';
import { create } from "domain";


// load bookings มาโชว์หน้า history
export async function load() {
    const res = await fetch('http://localhost:3000/bookings');
    const bookings = await res.json();

    if (!bookings) throw error(404);

    return {
        bookings
    };

}


export const actions = {
    delete: async ({ request }) => {
        try {
            const data = await request.formData();
            const trainId = data.get('trainid');
            const bookingId = data.get('id');

            // ดึงรายระเอียดการจอง
            const bookingRes = await fetch(`http://localhost:3000/bookings/${bookingId}`);
            if (!bookingRes.ok) {
                throw new Error('Failed to fetch booking data!');
            }
            const booking = await bookingRes.json();
            const passengers = booking.passenger;

            //ทำการลบ
            const deleteres = await fetch(`http://localhost:3000/bookings/${bookingId}`, {
                method: 'DELETE'
            });

            if (!deleteres.ok) {
                throw error(500, 'Failed to delete booking');
            }

            //ดึง data train มาเพื่อจะเอา available seat
            const trainRes = await fetch(`http://localhost:3000/trains/${trainId}`);
            if (!trainRes.ok) {
                throw new Error('Failed to fetch train data!');
            }
            const train = await trainRes.json();

            //ทำการ Update
            const updateRes = await fetch(`http://localhost:3000/trains/${trainId}`, {
                method: 'PATCH',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ availableSeats: train.availableSeats + passengers })
            });

            if (!updateRes.ok) {
                throw new Error('Failed to update available seats!');
            }

            return {
                success: true
            };
        } catch (error) {

        }
    }
};
