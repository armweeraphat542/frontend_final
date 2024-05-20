<script>
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';

    // @ts-ignore
    export let data;

    let booktrain = data.booktrain;
    let seats = booktrain.totalSeats;
    let passengers = 1;
    /**
	 * @type {any[]}
	 */
    let seatNumbers = [];


    //ให้เมื่อปุ่มทำการ fecth data ให้เรียบร้อยแล้วค่อย goto hisotry
    // @ts-ignore
    const handleSubmit = async (event) => {
        event.preventDefault();

        const formData = new FormData(event.target);
        const response = await fetch(event.target.action, {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            alert('Booking successful!');
            goto('/history');
        } else {
            alert('Booking failed!');
        }
    };

    onMount(() => {
        const params = new URLSearchParams(window.location.search);
        passengers = parseInt(params.get('passengers') || '1');
        BookingsGenerateSeats();
    });
    //ดึงข้อมูล bookings เพื่อจะดูเลขที่นั่ง
    async function BookingsGenerateSeats() {
        try {
            const res = await fetch(`http://localhost:3000/bookings`);
            const bookings = await res.json();
            generateSeatNumbers(bookings);//สุ่มเลขที่นั่ง
        } catch (error) {
            console.error('Error fetching existing bookings:', error);
        }
    }

    //สุ่มที่นั่ง แบบไม่ซ้ำเอาไปใช้กับ ที่ fecth data มาจากด้านบน
    // @ts-ignore
    function generateSeatNumbers(existingBookings) {
        seatNumbers = [];
        const bookedSeats = existingBookings
            // @ts-ignore
            .filter(booking => booking.trainid === booktrain.id)
            // @ts-ignore
            .flatMap(booking => booking.seatNumbers);

        for (let i = 0; i < passengers; i++) {
            let seatNo;
            do {
                seatNo = String(Math.floor(Math.random() * seats) + 1);
            } while (seatNumbers.includes(seatNo) || bookedSeats.includes(seatNo));
            seatNumbers.push(seatNo);
        }
    }
</script>
<!-- แสดงขบวนรถไฟ -->
<div class="train-info">
    <p><strong>Train Number:</strong> {booktrain.trainNumber}</p>
    <p><strong>Departure:</strong> {booktrain.departure}</p>
    <p><strong>Arrival:</strong> {booktrain.arrival}</p>
    <p><strong>Date:</strong> {booktrain.date}</p>
    <p><strong>Departure Time:</strong> {booktrain.departureTime}</p>
    <p><strong>Arrival Time:</strong> {booktrain.arrivalTime}</p>
    <p><strong>Duration:</strong> {booktrain.duration}</p>
    <p><strong>Available Seats:</strong> {booktrain.availableSeats}</p>
    <p><strong>Price:</strong> {booktrain.price}</p>
</div>


<!-- แบบฟอร์มให้หรอก -->
<div class="content">
    <h1>Booking</h1>
    <form method="POST" action="?/create" on:submit|preventDefault={handleSubmit}>
        <input type="hidden" name="trainId" value={booktrain.id} />
        <input type="hidden" name="passengers" value={passengers} />
        <div class="field">
            <label class="label">
                <span>Name</span>
                <div class="control">
                    <input name="name" class="input" type="text" placeholder="Name" required>
                </div>
            </label>
        </div>
        <div class="field">
            <label class="label">
                <span>Contact Number</span>
                <div class="control">
                    <input name="contactNumber" class="input" type="text" placeholder="Contact Number" required>
                </div>
            </label>
        </div>
        {#each seatNumbers as seatNumber, i}
        <div class="field">
            <label class="label">
                <span>Seat Number {i + 1}</span>
                <div class="control">
                    <input name="seatNumbers" value={seatNumber} class="input" type="text" readonly>
                </div>
            </label>
        </div>
        {/each}
        <button type="submit">Book now</button>
    </form>
</div>



<style>


    .train-info {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 20px auto;
        max-width: 600px;
    }

    .train-info p {
        margin: 5px 0;
    }

    .content {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 20px auto;
        max-width: 600px;
    }

    h1 {
        font-size: 24px;
        margin-bottom: 20px;
        text-align: center;
    }

    .field {
        margin-bottom: 15px;
    }

    .label {
        font-weight: bold;
        color: #333;
        display: block;
        margin-bottom: 5px;
    }

    .control {
        margin-top: 5px;
    }

    .input {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
    }

    button {
        width: 100%;
        padding: 10px 20px;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    button:hover {
        background-color: #0056b3;
    }


</style>


  