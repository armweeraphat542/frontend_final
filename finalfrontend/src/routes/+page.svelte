<script>
    import { onMount } from 'svelte';
    import { navigate } from 'svelte-routing';
    export let data;

    //เอาข้อมูล train ที่โหลดมาใส่และเอาไปใช้กับ function filterSearch
    let trains = data.trains;
    //เอาข้อมูลสถานีไปใส่ dropdown list
    let stations = data.stations;


    /**
	 * @type {any[]}
	 */
    let filteredTrains = [];
    let departure = '';
    let arrival = '';
    let date = '';
    let passengers = 1;

    function searchTrains() {
        // เปลี่ยน date ให้เป็นตาม database YYYY-MM-DD
        const formattedDate = date ? new Date(date).toISOString().split('T')[0] : '';
        
        // filter สถานีและวันที่ โดยข้อมูลไว้ใน filterTrains
        // @ts-ignore
        filteredTrains = trains.filter(train => {
            return (
                (!departure || train.departure === departure) && 
                (!arrival || train.arrival === arrival) &&
                (!date || train.date === formattedDate)
            );
        });
    }



    onMount(() => {
        // ให้แสดงเที่ยวรถไฟทั้งหมด
        filteredTrains = trains;
    });
</script>

<h1>Train Tickets</h1>

<div class="search-form">
    <label> 
        Departure:
        <select bind:value={departure}>
            <option value="">Select Departure</option>
            {#each stations as station}
            <option value={station}>{station}</option>
            {/each}
        </select>
    </label>
    <label>
        Arrival:
        <select bind:value={arrival}>
            <option value="">Select Arrival</option>
            {#each stations as station}
            <option value={station}>{station}</option>
            {/each}
        </select>
    </label>
    <label>
        Date:
        <input type="date" bind:value={date} />
    </label>
    <label>
        Passengers:
        <select bind:value={passengers}>
            {#each Array(4).fill(0).map((_, i) => i + 1) as passengerCount}
            <option value={passengerCount}>{passengerCount}</option>
            {/each}
        </select>
    </label>
    <button on:click={searchTrains}>Search</button>
</div>

<div class="train-list">
    {#each filteredTrains as train}
    <div class="train-item">
        <div class="train-info">
            <p><strong>Train Number:</strong> {train.trainNumber}</p>
            <p><strong>Departure:</strong> {train.departure}</p>
            <p><strong>Arrival:</strong> {train.arrival}</p>
            <p><strong>Date:</strong> {train.date}</p>
            <p><strong>Departure Time:</strong> {train.departureTime}</p>
            <p><strong>Arrival Time:</strong> {train.arrivalTime}</p>
            <p><strong>Duration:</strong> {train.duration}</p>
            <p><strong>Available Seats:</strong> {parseInt(train.availableSeats)}</p>
            <p><strong>Price:</strong> {train.price}</p>
        </div>
        <div class="action">
            <a href="/checkout?id={train.id}&passengers={passengers}">
                <button >Book</button>
            </a>
        </div>
    </div>
    {/each}
</div>

    


<style>
    h1 {
        text-align: center;
        margin-top: 20px;
        font-size: 2.5em;
        color: #333;
    }

    .search-form {
        max-width: 600px;
        margin: 20px auto;
        padding: 20px;
        background: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .search-form label {
        display: block;
        margin-bottom: 10px;
        color: #333;
    }

    .search-form select,
    .search-form input[type="date"] {
        width: 100%;
        padding: 8px;
        margin-top: 5px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    .search-form button {
        display: inline-block;
        margin-top: 15px;
        padding: 10px 15px;
        background-color: #007BFF;
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .search-form button:hover {
        background-color: #0056b3;
    }

    .train-list {
        max-width: 800px;
        margin: 20px auto;
        padding: 0;
        list-style: none;
    }

    .train-item {
        background: #fff;
        margin-bottom: 20px;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
    }

    .train-info {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;
        align-items: center;
        gap: 10px;
        margin-bottom: 20px;
    }

    .train-info p {
        margin: 5px 0;
        color: #555;
        white-space: nowrap;
    }

    .train-info p strong {
        color: #333;
    }

    .action {
        text-align: right;
    }

    .action a {
        text-decoration: none;
    }

    .action button {
        padding: 10px 15px;
        background-color: hsl(29, 81%, 51%);
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .action button:hover {
        background-color: #218838;
    }

</style>
  