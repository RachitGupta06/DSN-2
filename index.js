const notificationBtn = document.getElementById('enable');

  // Do an initial check to see what the notification permission state is
  if (Notification.permission === 'denied' || Notification.permission === 'default') {
    notificationBtn.style.display = 'block';
  } else {
    notificationBtn.style.display = 'none';
  }

  note.appendChild(createListItem('App initialised.'));