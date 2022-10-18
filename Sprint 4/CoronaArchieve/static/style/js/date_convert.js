// After Loading Page

document.addEventListener("DOMContentLoaded", function () {
  const timestampDateList = document.getElementsByClassName("timestamp-date");
  const timeDurationList = document.getElementsByClassName("time-duration");
  //   Find Difference between two dates

  for (let i = 0; i < timeDurationList.length; i++) {
    const timeDuration = timeDurationList[i];

    // Get Parent Element
    const keyDates = timeDuration.parentElement;

    const [startDate, endDate] =
      keyDates.getElementsByClassName("timestamp-date");

    const startDateValue = startDate.innerText;
    const endDateValue = endDate.innerText;

    // Difference between two dates
    const difference = Math.abs(
      new Date(startDateValue * 1000) - new Date(endDateValue * 1000)
    );

    // Difference in hours, minutes and seconds

    const hours = Math.floor(difference / 1000 / 60 / 60) % 24;
    const minutes = Math.floor(difference / 1000 / 60) % 60;
    const seconds = Math.floor(difference / 1000) % 60;

    // Display
    timeDuration.innerText = `${hours}h ${minutes}m ${seconds}s`;
  }

  for (let i = 0; i < timestampDateList.length; i++) {
    const timestampDate = timestampDateList[i];
    const timestamp = timestampDate.innerHTML;
    const date = new Date(timestamp * 1000);
    const dateString = date.toString();
    timestampDate.innerHTML = dateString;
  }
});
