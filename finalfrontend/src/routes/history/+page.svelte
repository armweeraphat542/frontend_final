<script>
    //เอา data ที่โหลดมา
    export let data;
    let bookings = data.bookings;
</script>

<h1 class="booking-history-title">Booking History</h1>

{#if bookings.length > 0}
    <ul class="booking-list">
        {#each bookings as booking}
            <li class="booking-item">
                <div class="booking-details">
                    <strong class="booking-label">Name:</strong> {booking.name} <br>
                    <strong class="booking-label">Contact Number:</strong> {booking.contactNumber} <br>
                    <strong class="booking-label">Train Number:</strong> {booking.trainNumber} <br>
                    <strong class="booking-label">Departure:</strong> {booking.departure} <br>
                    <strong class="booking-label">Arrival:</strong> {booking.arrival} <br>
                    <p><strong>Departure Time:</strong> {booking.departureTime}</p>
                    <p><strong>Arrival Time:</strong> {booking.arrivalTime}</p>
                    <strong class="booking-label">Passengers:</strong> {booking.passenger} <br>
                    <strong class="booking-label">Seat Numbers:</strong> 
                    {#each booking.seatNumbers as seatNumber, i}
                        {seatNumber}
                        {#if i !== booking.seatNumbers.length - 1}, {/if}
                    {/each} <br>
                    <strong class="booking-label">Total Price:</strong> {booking.totalprice} 
                    <form method="POST" action="?/delete" class="delete-form">
                        <input type="hidden" name="trainid" value={booking.trainid}>
                        <input type="hidden" name="id" value={booking.id}>
                        <button class="button" type="submit">ยกเลิกการจอง</button>
                    </form>
                </div>
            </li>
        {/each}
    </ul>
{:else}
    <p class="no-booking">No bookings found.</p>
{/if}

<style>
    .booking-history-title {
        font-size: 28px;
        margin-bottom: 20px;
        color: #2c3e50;
        text-align: center;
    }

    .booking-list {
        list-style: none;
        padding: 0;
        max-width: 800px;
        margin: 0 auto;
    }

    .booking-item {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        background-color: #f9f9f9;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s, box-shadow 0.2s;
    }




    .booking-details {
        line-height: 1.6;
    }

    .booking-label {
        font-weight: bold;
        color: #34495e;
    }

    .delete-form {
        margin-top: 10px;
    }

    .button {
        background-color: #e74c3c;
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .button:hover {
        background-color: #c0392b;
    }

    .no-booking {
        font-style: italic;
        color: #888;
        text-align: center;
    }
</style>
