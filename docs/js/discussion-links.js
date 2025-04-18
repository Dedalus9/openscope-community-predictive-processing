document.addEventListener('DOMContentLoaded', function() {
  // Skip if not on a content page
  if (!document.querySelector('.rst-content .document')) return;
  
  // Get the current page path and title
  const pathname = window.location.pathname;
  const basePath = '/openscope-community-predictive-processing/';
  let pagePath = pathname.startsWith(basePath) ? pathname.substring(basePath.length) : pathname;
  pagePath = pagePath.replace(/\/$/, '').replace(/\.html$/, '');
  if (pagePath === '') pagePath = 'index';
  
  const pageTitle = document.title.replace(' - OpenScope Community Predictive Processing', '');
  const searchQuery = encodeURIComponent(`Discussion: ${pageTitle} in:title repo:allenneuraldynamics/openscope-community-predictive-processing is:discussion`);
  
  // Create placeholder for discussion link
  const discussionContainer = document.createElement('div');
  discussionContainer.className = 'github-discussion-link';
  discussionContainer.innerHTML = '<hr><p>Loading discussion link...</p>';
  
  // Add styling
  const style = document.createElement('style');
  style.textContent = `
    .github-discussion-link {
      margin-top: 2rem;
      padding: 1rem 0;
    }
    .github-discussion-link a {
      display: inline-block;
      padding: 0.5rem 1rem;
      border: 1px solid #ddd;
      border-radius: 4px;
      text-decoration: none;
    }
    .github-discussion-link a:hover {
      background-color: #f5f5f5;
    }
    .github-discussion-link .login-note {
      font-size: 0.8rem;
      color: #666;
      margin-top: 0.5rem;
    }
  `;
  document.head.appendChild(style);
  
  // Add to page
  const content = document.querySelector('.rst-content .document');
  if (content) {
    content.appendChild(discussionContainer);
  }
  
  // Search for existing discussions
  fetch(`https://api.github.com/search/issues?q=${searchQuery}`)
    .then(response => response.json())
    .then(data => {
      let linkHtml = '';
      
      if (data.items && data.items.length > 0) {
        // Found an existing discussion
        const discussion = data.items[0];
        linkHtml = `
          <p>
            <a href="${discussion.html_url}" target="_blank">
              💬 Join the discussion for this page on GitHub
            </a>
          </p>
        `;
      } else {
        // No discussion exists - create new one
        linkHtml = `
          <p>
            <a href="https://github.com/allenneuraldynamics/openscope-community-predictive-processing/discussions/new?category=q-a&title=Discussion: ${encodeURIComponent(pageTitle)}" target="_blank">
              💬 Start a discussion for this page on GitHub
            </a>
            <span class="login-note">(A GitHub account is required to create or participate in discussions)</span>
          </p>
        `;
      }
      
      discussionContainer.innerHTML = `<hr>${linkHtml}`;
    })
    .catch(error => {
      // Fall back to creating new discussions
      discussionContainer.innerHTML = `
        <hr>
        <p>
          <a href="https://github.com/allenneuraldynamics/openscope-community-predictive-processing/discussions/new?category=q-a&title=Discussion: ${encodeURIComponent(pageTitle)}" target="_blank">
            💬 Discuss this page on GitHub
          </a>
          <span class="login-note">(A GitHub account is required to create or participate in discussions)</span>
        </p>
      `;
    });
});